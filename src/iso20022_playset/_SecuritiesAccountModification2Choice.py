# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketSpecificAttribute1
from . import SystemRestriction1
from . import SystemSecuritiesAccount5

class SecuritiesAccountModification2Choice(base_types._BaseFieldType):

	__slots__ = ["_MktSpcfcAttr", "_SysRstrctn", "_SysSctiesAcct"]
	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, False)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, False)

	@property
	def SysRstrctn(self):
		return self._SysRstrctn

	@SysRstrctn.setter
	def SysRstrctn(self, value):
		self._SysRstrctn = value if value is not None else base_types.UninitialisedField(self, 'SysRstrctn', SystemRestriction1, False)

	@SysRstrctn.deleter
	def SysRstrctn(self):
		del self._SysRstrctn
		self._SysRstrctn = base_types.UninitialisedField(self, 'SysRstrctn', SystemRestriction1, False)

	@property
	def SysSctiesAcct(self):
		return self._SysSctiesAcct

	@SysSctiesAcct.setter
	def SysSctiesAcct(self, value):
		self._SysSctiesAcct = value if value is not None else base_types.UninitialisedField(self, 'SysSctiesAcct', SystemSecuritiesAccount5, False)

	@SysSctiesAcct.deleter
	def SysSctiesAcct(self):
		del self._SysSctiesAcct
		self._SysSctiesAcct = base_types.UninitialisedField(self, 'SysSctiesAcct', SystemSecuritiesAccount5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysRstrctn', type=SystemRestriction1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysSctiesAcct', type=SystemSecuritiesAccount5, min=0, max=1, mutex_group=1, array=False),
	))