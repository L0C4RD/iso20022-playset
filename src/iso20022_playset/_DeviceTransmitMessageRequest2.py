# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100KBinary
from . import NetworkParameters7
from . import Number

class DeviceTransmitMessageRequest2(base_types._BaseFieldType):

	__slots__ = ["_DstnAdr", "_MaxTrnsmssnTm", "_MaxWtgTm", "_MsgToSnd"]
	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if value is not None else base_types.UninitialisedField(self, 'DstnAdr', NetworkParameters7, False)

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = base_types.UninitialisedField(self, 'DstnAdr', NetworkParameters7, False)

	@property
	def MaxTrnsmssnTm(self):
		return self._MaxTrnsmssnTm

	@MaxTrnsmssnTm.setter
	def MaxTrnsmssnTm(self, value):
		self._MaxTrnsmssnTm = value if value is not None else base_types.UninitialisedField(self, 'MaxTrnsmssnTm', Number, False)

	@MaxTrnsmssnTm.deleter
	def MaxTrnsmssnTm(self):
		del self._MaxTrnsmssnTm
		self._MaxTrnsmssnTm = base_types.UninitialisedField(self, 'MaxTrnsmssnTm', Number, False)

	@property
	def MaxWtgTm(self):
		return self._MaxWtgTm

	@MaxWtgTm.setter
	def MaxWtgTm(self, value):
		self._MaxWtgTm = value if value is not None else base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@MaxWtgTm.deleter
	def MaxWtgTm(self):
		del self._MaxWtgTm
		self._MaxWtgTm = base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@property
	def MsgToSnd(self):
		return self._MsgToSnd

	@MsgToSnd.setter
	def MsgToSnd(self, value):
		self._MsgToSnd = value if value is not None else base_types.UninitialisedField(self, 'MsgToSnd', Max100KBinary, False)

	@MsgToSnd.deleter
	def MsgToSnd(self):
		del self._MsgToSnd
		self._MsgToSnd = base_types.UninitialisedField(self, 'MsgToSnd', Max100KBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DstnAdr', type=NetworkParameters7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxTrnsmssnTm', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToSnd', type=Max100KBinary, min=1, max=1, mutex_group=None, array=False),
	))