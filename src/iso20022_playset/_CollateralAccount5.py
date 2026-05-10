from . import base_types
from ._MarginAccount1 import MarginAccount1
from ._PartyIdentification118Choice import PartyIdentification118Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class CollateralAccount5(base_types._BaseFieldType):

	__slots__ = ["_CollSgrtnByVal", "_Id", "_RltdMrgnAcct", "_TitlTrfCollArrgmnt"]
	@property
	def CollSgrtnByVal(self):
		return self._CollSgrtnByVal

	@CollSgrtnByVal.setter
	def CollSgrtnByVal(self, value):
		self._CollSgrtnByVal = value if type(value) != base_types.auto else self.make_default("CollSgrtnByVal")

	@CollSgrtnByVal.deleter
	def CollSgrtnByVal(self):
		del self._CollSgrtnByVal
		self._CollSgrtnByVal = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RltdMrgnAcct(self):
		return self._RltdMrgnAcct

	@RltdMrgnAcct.setter
	def RltdMrgnAcct(self, value):
		self._RltdMrgnAcct = value if type(value) != base_types.auto else self.make_default("RltdMrgnAcct")

	@RltdMrgnAcct.deleter
	def RltdMrgnAcct(self):
		del self._RltdMrgnAcct
		self._RltdMrgnAcct = None

	@property
	def TitlTrfCollArrgmnt(self):
		return self._TitlTrfCollArrgmnt

	@TitlTrfCollArrgmnt.setter
	def TitlTrfCollArrgmnt(self, value):
		self._TitlTrfCollArrgmnt = value if type(value) != base_types.auto else self.make_default("TitlTrfCollArrgmnt")

	@TitlTrfCollArrgmnt.deleter
	def TitlTrfCollArrgmnt(self):
		del self._TitlTrfCollArrgmnt
		self._TitlTrfCollArrgmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSgrtnByVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMrgnAcct', type=MarginAccount1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TitlTrfCollArrgmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

