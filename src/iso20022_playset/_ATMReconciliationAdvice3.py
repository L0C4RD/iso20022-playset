# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand8
from . import ATMCommand9
from . import ATMEnvironment22
from . import ATMTransaction36

class ATMReconciliationAdvice3(base_types._BaseFieldType):

	__slots__ = ["_CmdCntxt", "_CmdRslt", "_Envt", "_Tx"]
	@property
	def CmdCntxt(self):
		return self._CmdCntxt

	@CmdCntxt.setter
	def CmdCntxt(self, value):
		self._CmdCntxt = value if value is not None else base_types.UninitialisedField(self, 'CmdCntxt', ATMCommand9, False)

	@CmdCntxt.deleter
	def CmdCntxt(self):
		del self._CmdCntxt
		self._CmdCntxt = base_types.UninitialisedField(self, 'CmdCntxt', ATMCommand9, False)

	@property
	def CmdRslt(self):
		return self._CmdRslt

	@CmdRslt.setter
	def CmdRslt(self, value):
		self._CmdRslt = value if value is not None else base_types.UninitialisedField(self, 'CmdRslt', ATMCommand8, True)

	@CmdRslt.deleter
	def CmdRslt(self):
		del self._CmdRslt
		self._CmdRslt = base_types.UninitialisedField(self, 'CmdRslt', ATMCommand8, True)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment22, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment22, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', ATMTransaction36, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', ATMTransaction36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmdCntxt', type=ATMCommand9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdRslt', type=ATMCommand8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=ATMTransaction36, min=1, max=1, mutex_group=None, array=False),
	))