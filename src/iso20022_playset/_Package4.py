from . import base_types
from ._SecuritiesTransactionPrice17Choice import SecuritiesTransactionPrice17Choice
from ._SecuritiesTransactionPrice20Choice import SecuritiesTransactionPrice20Choice
from ._Max100Text import Max100Text

class Package4(base_types._BaseFieldType):

	__slots__ = ["_Pric", "_Sprd", "_FxSwpLkId", "_CmplxTradId"]
	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def FxSwpLkId(self):
		return self._FxSwpLkId

	@FxSwpLkId.setter
	def FxSwpLkId(self, value):
		self._FxSwpLkId = value if type(value) != base_types.auto else self.make_default("FxSwpLkId")

	@FxSwpLkId.deleter
	def FxSwpLkId(self):
		del self._FxSwpLkId
		self._FxSwpLkId = None

	@property
	def CmplxTradId(self):
		return self._CmplxTradId

	@CmplxTradId.setter
	def CmplxTradId(self, value):
		self._CmplxTradId = value if type(value) != base_types.auto else self.make_default("CmplxTradId")

	@CmplxTradId.deleter
	def CmplxTradId(self):
		del self._CmplxTradId
		self._CmplxTradId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxSwpLkId', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplxTradId', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
	))

