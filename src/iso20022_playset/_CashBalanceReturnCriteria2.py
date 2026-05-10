from . import base_types
from ._RequestedIndicator import RequestedIndicator

class CashBalanceReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_NbOfPmtsInd", "_ValDtInd", "_PrcgDtInd", "_StsInd", "_TpInd"]
	@property
	def NbOfPmtsInd(self):
		return self._NbOfPmtsInd

	@NbOfPmtsInd.setter
	def NbOfPmtsInd(self, value):
		self._NbOfPmtsInd = value if type(value) != base_types.auto else self.make_default("NbOfPmtsInd")

	@NbOfPmtsInd.deleter
	def NbOfPmtsInd(self):
		del self._NbOfPmtsInd
		self._NbOfPmtsInd = None

	@property
	def ValDtInd(self):
		return self._ValDtInd

	@ValDtInd.setter
	def ValDtInd(self, value):
		self._ValDtInd = value if type(value) != base_types.auto else self.make_default("ValDtInd")

	@ValDtInd.deleter
	def ValDtInd(self):
		del self._ValDtInd
		self._ValDtInd = None

	@property
	def PrcgDtInd(self):
		return self._PrcgDtInd

	@PrcgDtInd.setter
	def PrcgDtInd(self, value):
		self._PrcgDtInd = value if type(value) != base_types.auto else self.make_default("PrcgDtInd")

	@PrcgDtInd.deleter
	def PrcgDtInd(self):
		del self._PrcgDtInd
		self._PrcgDtInd = None

	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if type(value) != base_types.auto else self.make_default("StsInd")

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = None

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if type(value) != base_types.auto else self.make_default("TpInd")

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfPmtsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDtInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))

