import base_types
import ExtendOrPayQuery1
import PartyAndSignature2

class ExtendOrPayRequestV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_XtndOrPayReqDtls"]
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
	def XtndOrPayReqDtls(self):
		return self._XtndOrPayReqDtls

	@XtndOrPayReqDtls.setter
	def XtndOrPayReqDtls(self, value):
		self._XtndOrPayReqDtls = value if type(value) != auto else self.make_default("XtndOrPayReqDtls")

	@XtndOrPayReqDtls.deleter
	def XtndOrPayReqDtls(self):
		del self._XtndOrPayReqDtls
		self._XtndOrPayReqDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndOrPayReqDtls', type=ExtendOrPayQuery1, min=1, max=1, mutex_group=None, array=False),
	))

