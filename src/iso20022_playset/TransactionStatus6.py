from . import base_types
import CollateralStatus1Code
import CollateralStatus2Choice

class TransactionStatus6(base_types._BaseFieldType):

	__slots__ = ["_ExctnSts", "_CvrgSts"]
	@property
	def ExctnSts(self):
		return self._ExctnSts

	@ExctnSts.setter
	def ExctnSts(self, value):
		self._ExctnSts = value if type(value) != auto else self.make_default("ExctnSts")

	@ExctnSts.deleter
	def ExctnSts(self):
		del self._ExctnSts
		self._ExctnSts = None

	@property
	def CvrgSts(self):
		return self._CvrgSts

	@CvrgSts.setter
	def CvrgSts(self, value):
		self._CvrgSts = value if type(value) != auto else self.make_default("CvrgSts")

	@CvrgSts.deleter
	def CvrgSts(self):
		del self._CvrgSts
		self._CvrgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctnSts', type=CollateralStatus2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvrgSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))

