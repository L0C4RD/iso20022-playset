# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMSecurityConfiguration2
from . import ATMSecurityConfiguration3
from . import ATMSecurityConfiguration4
from . import ATMSecurityConfiguration5
from . import Algorithm11Code
from . import Algorithm12Code
from . import MessageProtection1Code

class ATMSecurityConfiguration1(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_DgtlSgntr", "_Keys", "_MACAlgo", "_MsgPrtcn", "_Ncrptn", "_PIN"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', Algorithm11Code, True)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', Algorithm11Code, True)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', ATMSecurityConfiguration4, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', ATMSecurityConfiguration4, False)

	@property
	def Keys(self):
		return self._Keys

	@Keys.setter
	def Keys(self, value):
		self._Keys = value if value is not None else base_types.UninitialisedField(self, 'Keys', ATMSecurityConfiguration2, False)

	@Keys.deleter
	def Keys(self):
		del self._Keys
		self._Keys = base_types.UninitialisedField(self, 'Keys', ATMSecurityConfiguration2, False)

	@property
	def MACAlgo(self):
		return self._MACAlgo

	@MACAlgo.setter
	def MACAlgo(self, value):
		self._MACAlgo = value if value is not None else base_types.UninitialisedField(self, 'MACAlgo', Algorithm12Code, True)

	@MACAlgo.deleter
	def MACAlgo(self):
		del self._MACAlgo
		self._MACAlgo = base_types.UninitialisedField(self, 'MACAlgo', Algorithm12Code, True)

	@property
	def MsgPrtcn(self):
		return self._MsgPrtcn

	@MsgPrtcn.setter
	def MsgPrtcn(self, value):
		self._MsgPrtcn = value if value is not None else base_types.UninitialisedField(self, 'MsgPrtcn', MessageProtection1Code, True)

	@MsgPrtcn.deleter
	def MsgPrtcn(self):
		del self._MsgPrtcn
		self._MsgPrtcn = base_types.UninitialisedField(self, 'MsgPrtcn', MessageProtection1Code, True)

	@property
	def Ncrptn(self):
		return self._Ncrptn

	@Ncrptn.setter
	def Ncrptn(self, value):
		self._Ncrptn = value if value is not None else base_types.UninitialisedField(self, 'Ncrptn', ATMSecurityConfiguration3, False)

	@Ncrptn.deleter
	def Ncrptn(self):
		del self._Ncrptn
		self._Ncrptn = base_types.UninitialisedField(self, 'Ncrptn', ATMSecurityConfiguration3, False)

	@property
	def PIN(self):
		return self._PIN

	@PIN.setter
	def PIN(self, value):
		self._PIN = value if value is not None else base_types.UninitialisedField(self, 'PIN', ATMSecurityConfiguration5, False)

	@PIN.deleter
	def PIN(self):
		del self._PIN
		self._PIN = base_types.UninitialisedField(self, 'PIN', ATMSecurityConfiguration5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=ATMSecurityConfiguration4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Keys', type=ATMSecurityConfiguration2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MACAlgo', type=Algorithm12Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPrtcn', type=MessageProtection1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ncrptn', type=ATMSecurityConfiguration3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PIN', type=ATMSecurityConfiguration5, min=0, max=1, mutex_group=None, array=False),
	))