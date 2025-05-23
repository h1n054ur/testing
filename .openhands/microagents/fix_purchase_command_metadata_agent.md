---
triggers:
  - fix purchase command missing metadata
  - refetch metadata after purchasing number
  - twilio-manager purchase returns unknown country or type
agent: CodeActAgent
---

# 1) Add get_number_metadata to TwilioGateway
- File: app/gateways/twilio_gateway.py
- Add method:

  def get_number_metadata(self, phone_number: str):
      try:
          numbers = self._client.incoming_phone_numbers.list(phone_number=phone_number)
          if not numbers:
              return None
          number = numbers[0]
          return {
              "number": number.phone_number,
              "sid": number.sid,
              "friendly_name": number.friendly_name,
              "capabilities": number.capabilities,
              "iso_country": getattr(number, "iso_country", "Unknown"),
              "region": getattr(number, "region", "N/A"),
              "type": self._infer_type(number.capabilities)
          }
      except TwilioRestException as e:
          print(f"Error fetching number metadata: {e}")
          return None

# 2) Add helper to TwilioGateway
- Still in app/gateways/twilio_gateway.py
- Add this below the above method:

  def _infer_type(self, capabilities):
      if capabilities.get("voice") and capabilities.get("sms"):
          return "local"
      elif capabilities.get("sms") and not capabilities.get("voice"):
          return "mobile"
      elif capabilities.get("voice") and not capabilities.get("sms"):
          return "tollfree"
      return "N/A"

# 3) Update purchase_exact_number to re-fetch metadata
- File: app/core/purchase.py
- Replace purchase_exact_number method with:

  def purchase_exact_number(self, number: str):
      result = self.twilio_gateway.purchase_number(number)
      if not result.get("success"):
          return {"success": False, "message": result.get("error", "Purchase failed")}

      metadata = self.twilio_gateway.get_number_metadata(number)
      if not metadata or metadata.get("country") == "Unknown":
          return {"success": True, "message": f"Purchased {number}, but metadata is incomplete (try again later)."}

      return {
          "success": True,
          "message": f"Successfully purchased {metadata['number']} ({metadata['type']}) in {metadata['iso_country']}"
      }

# 4) Log decision
log_decision3{
  "context": "cli-purchase-fix",
  "decision": "purchase_exact_number now re-fetches metadata from Twilio after buying a number to ensure manage view shows complete country/type info"
}
