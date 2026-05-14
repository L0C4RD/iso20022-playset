# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMCommand15 import ATMCommand15
from ._ATMCommand16 import ATMCommand16
from ._ATMEnvironment6 import ATMEnvironment6
from ._ATMSecurityContext5 import ATMSecurityContext5
from ._ATMStatus2 import ATMStatus2

class ATMDeviceReport4(base_types._BaseFieldType):

	__slots__ = ["_ATMGblSts", "_ATMSctyCntxt", "_CmdCntxt", "_CmdRslt", "_Envt"]
	@property
	def ATMGblSts(self):
		return self._ATMGblSts

	@ATMGblSts.setter
	def ATMGblSts(self, value):
		self._ATMGblSts = value if type(value) != base_types.auto else self.make_default("ATMGblSts")

	@ATMGblSts.deleter
	def ATMGblSts(self):
		del self._ATMGblSts
		self._ATMGblSts = None

	@property
	def ATMSctyCntxt(self):
		return self._ATMSctyCntxt

	@ATMSctyCntxt.setter
	def ATMSctyCntxt(self, value):
		self._ATMSctyCntxt = value if type(value) != base_types.auto else self.make_default("ATMSctyCntxt")

	@ATMSctyCntxt.deleter
	def ATMSctyCntxt(self):
		del self._ATMSctyCntxt
		self._ATMSctyCntxt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMGblSts', type=ATMStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSctyCntxt', type=ATMSecurityContext5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdCntxt', type=ATMCommand16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdRslt', type=ATMCommand15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment6, min=1, max=1, mutex_group=None, array=False),
	))