import base_types
import RequestedIndicator

class CollateralValueReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctInd", "_SctiesAcctOwnrInd", "_CshAcctSvcrInd", "_Scties", "_SctiesAcctSvcrInd", "_CshAcctOwnrInd", "_TtlCollValtnInd"]
	@property
	def SctiesAcctInd(self):
		return self._SctiesAcctInd

	@SctiesAcctInd.setter
	def SctiesAcctInd(self, value):
		self._SctiesAcctInd = value if type(value) != auto else self.make_default("SctiesAcctInd")

	@SctiesAcctInd.deleter
	def SctiesAcctInd(self):
		del self._SctiesAcctInd
		self._SctiesAcctInd = None

	@property
	def SctiesAcctOwnrInd(self):
		return self._SctiesAcctOwnrInd

	@SctiesAcctOwnrInd.setter
	def SctiesAcctOwnrInd(self, value):
		self._SctiesAcctOwnrInd = value if type(value) != auto else self.make_default("SctiesAcctOwnrInd")

	@SctiesAcctOwnrInd.deleter
	def SctiesAcctOwnrInd(self):
		del self._SctiesAcctOwnrInd
		self._SctiesAcctOwnrInd = None

	@property
	def CshAcctSvcrInd(self):
		return self._CshAcctSvcrInd

	@CshAcctSvcrInd.setter
	def CshAcctSvcrInd(self, value):
		self._CshAcctSvcrInd = value if type(value) != auto else self.make_default("CshAcctSvcrInd")

	@CshAcctSvcrInd.deleter
	def CshAcctSvcrInd(self):
		del self._CshAcctSvcrInd
		self._CshAcctSvcrInd = None

	@property
	def Scties(self):
		return self._Scties

	@Scties.setter
	def Scties(self, value):
		self._Scties = value if type(value) != auto else self.make_default("Scties")

	@Scties.deleter
	def Scties(self):
		del self._Scties
		self._Scties = None

	@property
	def SctiesAcctSvcrInd(self):
		return self._SctiesAcctSvcrInd

	@SctiesAcctSvcrInd.setter
	def SctiesAcctSvcrInd(self, value):
		self._SctiesAcctSvcrInd = value if type(value) != auto else self.make_default("SctiesAcctSvcrInd")

	@SctiesAcctSvcrInd.deleter
	def SctiesAcctSvcrInd(self):
		del self._SctiesAcctSvcrInd
		self._SctiesAcctSvcrInd = None

	@property
	def CshAcctOwnrInd(self):
		return self._CshAcctOwnrInd

	@CshAcctOwnrInd.setter
	def CshAcctOwnrInd(self, value):
		self._CshAcctOwnrInd = value if type(value) != auto else self.make_default("CshAcctOwnrInd")

	@CshAcctOwnrInd.deleter
	def CshAcctOwnrInd(self):
		del self._CshAcctOwnrInd
		self._CshAcctOwnrInd = None

	@property
	def TtlCollValtnInd(self):
		return self._TtlCollValtnInd

	@TtlCollValtnInd.setter
	def TtlCollValtnInd(self, value):
		self._TtlCollValtnInd = value if type(value) != auto else self.make_default("TtlCollValtnInd")

	@TtlCollValtnInd.deleter
	def TtlCollValtnInd(self):
		del self._TtlCollValtnInd
		self._TtlCollValtnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scties', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCollValtnInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

