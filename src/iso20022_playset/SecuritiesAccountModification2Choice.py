import base_types
import SystemRestriction1
import SystemSecuritiesAccount5
import MarketSpecificAttribute1

class SecuritiesAccountModification2Choice(base_types._BaseFieldType):

	__slots__ = ["_MktSpcfcAttr", "_SysSctiesAcct", "_SysRstrctn"]
	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if type(value) != auto else self.make_default("MktSpcfcAttr")

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = None

	@property
	def SysSctiesAcct(self):
		return self._SysSctiesAcct

	@SysSctiesAcct.setter
	def SysSctiesAcct(self, value):
		self._SysSctiesAcct = value if type(value) != auto else self.make_default("SysSctiesAcct")

	@SysSctiesAcct.deleter
	def SysSctiesAcct(self):
		del self._SysSctiesAcct
		self._SysSctiesAcct = None

	@property
	def SysRstrctn(self):
		return self._SysRstrctn

	@SysRstrctn.setter
	def SysRstrctn(self, value):
		self._SysRstrctn = value if type(value) != auto else self.make_default("SysRstrctn")

	@SysRstrctn.deleter
	def SysRstrctn(self):
		del self._SysRstrctn
		self._SysRstrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysSctiesAcct', type=SystemSecuritiesAccount5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysRstrctn', type=SystemRestriction1, min=0, max=1, mutex_group=1, array=False),
	))

