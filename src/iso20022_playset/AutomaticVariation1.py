from . import base_types
import Max35Text
import Max2000Text
import VariationType1Code
import AmountAndTrigger1

class AutomaticVariation1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_AddtlInf", "_AmtAndTrggr", "_Id"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AmtAndTrggr(self):
		return self._AmtAndTrggr

	@AmtAndTrggr.setter
	def AmtAndTrggr(self, value):
		self._AmtAndTrggr = value if type(value) != auto else self.make_default("AmtAndTrggr")

	@AmtAndTrggr.deleter
	def AmtAndTrggr(self):
		del self._AmtAndTrggr
		self._AmtAndTrggr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=VariationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtAndTrggr', type=AmountAndTrigger1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

