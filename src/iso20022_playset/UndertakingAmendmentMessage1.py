import base_types
import Amendment1
import PartyAndSignature2

class UndertakingAmendmentMessage1(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def UdrtkgAmdmntDtls(self):
		return self._UdrtkgAmdmntDtls

	@UdrtkgAmdmntDtls.setter
	def UdrtkgAmdmntDtls(self, value):
		self._UdrtkgAmdmntDtls = value if type(value) != auto else self.make_default("UdrtkgAmdmntDtls")

	@UdrtkgAmdmntDtls.deleter
	def UdrtkgAmdmntDtls(self):
		del self._UdrtkgAmdmntDtls
		self._UdrtkgAmdmntDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntDtls', type=Amendment1, min=1, max=1, mutex_group=None, array=False),
	))

