from . import base_types
from ._ATMSecurityConfiguration5 import ATMSecurityConfiguration5
from ._ATMSecurityConfiguration4 import ATMSecurityConfiguration4
from ._ATMSecurityConfiguration2 import ATMSecurityConfiguration2
from ._ATMSecurityConfiguration3 import ATMSecurityConfiguration3
from ._MessageProtection1Code import MessageProtection1Code
from ._Algorithm12Code import Algorithm12Code
from ._Algorithm11Code import Algorithm11Code

class ATMSecurityConfiguration1(base_types._BaseFieldType):

	__slots__ = ["_MACAlgo", "_PIN", "_DgstAlgo", "_Ncrptn", "_Keys", "_MsgPrtcn", "_DgtlSgntr"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != base_types.auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def Keys(self):
		return self._Keys

	@Keys.setter
	def Keys(self, value):
		self._Keys = value if type(value) != base_types.auto else self.make_default("Keys")

	@Keys.deleter
	def Keys(self):
		del self._Keys
		self._Keys = None

	@property
	def MACAlgo(self):
		return self._MACAlgo

	@MACAlgo.setter
	def MACAlgo(self, value):
		self._MACAlgo = value if type(value) != base_types.auto else self.make_default("MACAlgo")

	@MACAlgo.deleter
	def MACAlgo(self):
		del self._MACAlgo
		self._MACAlgo = None

	@property
	def MsgPrtcn(self):
		return self._MsgPrtcn

	@MsgPrtcn.setter
	def MsgPrtcn(self, value):
		self._MsgPrtcn = value if type(value) != base_types.auto else self.make_default("MsgPrtcn")

	@MsgPrtcn.deleter
	def MsgPrtcn(self):
		del self._MsgPrtcn
		self._MsgPrtcn = None

	@property
	def Ncrptn(self):
		return self._Ncrptn

	@Ncrptn.setter
	def Ncrptn(self, value):
		self._Ncrptn = value if type(value) != base_types.auto else self.make_default("Ncrptn")

	@Ncrptn.deleter
	def Ncrptn(self):
		del self._Ncrptn
		self._Ncrptn = None

	@property
	def PIN(self):
		return self._PIN

	@PIN.setter
	def PIN(self, value):
		self._PIN = value if type(value) != base_types.auto else self.make_default("PIN")

	@PIN.deleter
	def PIN(self):
		del self._PIN
		self._PIN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=ATMSecurityConfiguration4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Keys', type=ATMSecurityConfiguration2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MACAlgo', type=Algorithm12Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPrtcn', type=MessageProtection1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ncrptn', type=ATMSecurityConfiguration3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PIN', type=ATMSecurityConfiguration5, min=0, max=1, mutex_group=None, array=False),
	))

