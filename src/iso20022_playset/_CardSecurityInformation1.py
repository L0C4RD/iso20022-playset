from . import base_types
from ._CSCManagement1Code import CSCManagement1Code
from ._Min3Max4NumericText import Min3Max4NumericText

class CardSecurityInformation1(base_types._BaseFieldType):

	__slots__ = ["_CSCMgmt", "_CSCVal"]
	@property
	def CSCMgmt(self):
		return self._CSCMgmt

	@CSCMgmt.setter
	def CSCMgmt(self, value):
		self._CSCMgmt = value if type(value) != base_types.auto else self.make_default("CSCMgmt")

	@CSCMgmt.deleter
	def CSCMgmt(self):
		del self._CSCMgmt
		self._CSCMgmt = None

	@property
	def CSCVal(self):
		return self._CSCVal

	@CSCVal.setter
	def CSCVal(self, value):
		self._CSCVal = value if type(value) != base_types.auto else self.make_default("CSCVal")

	@CSCVal.deleter
	def CSCVal(self):
		del self._CSCVal
		self._CSCVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSCMgmt', type=CSCManagement1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CSCVal', type=Min3Max4NumericText, min=0, max=1, mutex_group=None, array=False),
	))

