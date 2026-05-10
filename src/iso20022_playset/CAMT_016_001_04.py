import base_types
import GetCurrencyExchangeRateV04

class CAMT_016_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetCcyXchgRate"]
		@property
		def GetCcyXchgRate(self):
			return self._GetCcyXchgRate

		@GetCcyXchgRate.setter
		def GetCcyXchgRate(self, value):
			self._GetCcyXchgRate = value if type(value) != auto else self.make_default("GetCcyXchgRate")

		@GetCcyXchgRate.deleter
		def GetCcyXchgRate(self):
			del self._GetCcyXchgRate
			self._GetCcyXchgRate = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetCcyXchgRate', type=GetCurrencyExchangeRateV04, min=1, max=1, mutex_group=None, array=False),
		))

