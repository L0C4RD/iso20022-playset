import base_types
import ExtendOrPayQuery2
import PartyAndSignature2

class ExtendOrPayResponseV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_XtndOrPayRspnDtls"]
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
	def XtndOrPayRspnDtls(self):
		return self._XtndOrPayRspnDtls

	@XtndOrPayRspnDtls.setter
	def XtndOrPayRspnDtls(self, value):
		self._XtndOrPayRspnDtls = value if type(value) != auto else self.make_default("XtndOrPayRspnDtls")

	@XtndOrPayRspnDtls.deleter
	def XtndOrPayRspnDtls(self):
		del self._XtndOrPayRspnDtls
		self._XtndOrPayRspnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndOrPayRspnDtls', type=ExtendOrPayQuery2, min=1, max=1, mutex_group=None, array=False),
	))

