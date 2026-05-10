from . import base_types
from ._ATMCommand8 import ATMCommand8
from ._ATMCommand9 import ATMCommand9
from ._ATMEnvironment22 import ATMEnvironment22
from ._ATMTransaction36 import ATMTransaction36

class ATMReconciliationAdvice3(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_CmdCntxt", "_Tx", "_CmdRslt"]
	@property
	def CmdCntxt(self):
		return self._CmdCntxt

	@CmdCntxt.setter
	def CmdCntxt(self, value):
		self._CmdCntxt = value if type(value) != base_types.auto else self.make_default("CmdCntxt")

	@CmdCntxt.deleter
	def CmdCntxt(self):
		del self._CmdCntxt
		self._CmdCntxt = None

	@property
	def CmdRslt(self):
		return self._CmdRslt

	@CmdRslt.setter
	def CmdRslt(self, value):
		self._CmdRslt = value if type(value) != base_types.auto else self.make_default("CmdRslt")

	@CmdRslt.deleter
	def CmdRslt(self):
		del self._CmdRslt
		self._CmdRslt = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmdCntxt', type=ATMCommand9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdRslt', type=ATMCommand8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=ATMTransaction36, min=1, max=1, mutex_group=None, array=False),
	))

