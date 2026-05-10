import base_types
import ClaimNonReceiptV10

class CAMT_027_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ClmNonRct"]
		@property
		def ClmNonRct(self):
			return self._ClmNonRct

		@ClmNonRct.setter
		def ClmNonRct(self, value):
			self._ClmNonRct = value if type(value) != auto else self.make_default("ClmNonRct")

		@ClmNonRct.deleter
		def ClmNonRct(self):
			del self._ClmNonRct
			self._ClmNonRct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClmNonRct', type=ClaimNonReceiptV10, min=1, max=1, mutex_group=None, array=False),
		))

