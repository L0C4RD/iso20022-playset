# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCounterType3Code
from . import ImpliedCurrencyAndAmount
from . import Number

class ATMCassetteCounters5(base_types._BaseFieldType):

	__slots__ = ["_AddedNb", "_DpstdAmt", "_DpstdNb", "_DspnsdNb", "_InitlAmt", "_InitlNb", "_PresntdNb", "_RcycldNb", "_RjctdNb", "_RmvdAmt", "_RmvdNb", "_RtrctdAmt", "_RtrctdNb", "_Tp"]
	@property
	def AddedNb(self):
		return self._AddedNb

	@AddedNb.setter
	def AddedNb(self, value):
		self._AddedNb = value if value is not None else base_types.UninitialisedField(self, 'AddedNb', Number, False)

	@AddedNb.deleter
	def AddedNb(self):
		del self._AddedNb
		self._AddedNb = base_types.UninitialisedField(self, 'AddedNb', Number, False)

	@property
	def DpstdAmt(self):
		return self._DpstdAmt

	@DpstdAmt.setter
	def DpstdAmt(self, value):
		self._DpstdAmt = value if value is not None else base_types.UninitialisedField(self, 'DpstdAmt', ImpliedCurrencyAndAmount, False)

	@DpstdAmt.deleter
	def DpstdAmt(self):
		del self._DpstdAmt
		self._DpstdAmt = base_types.UninitialisedField(self, 'DpstdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def DpstdNb(self):
		return self._DpstdNb

	@DpstdNb.setter
	def DpstdNb(self, value):
		self._DpstdNb = value if value is not None else base_types.UninitialisedField(self, 'DpstdNb', Number, False)

	@DpstdNb.deleter
	def DpstdNb(self):
		del self._DpstdNb
		self._DpstdNb = base_types.UninitialisedField(self, 'DpstdNb', Number, False)

	@property
	def DspnsdNb(self):
		return self._DspnsdNb

	@DspnsdNb.setter
	def DspnsdNb(self, value):
		self._DspnsdNb = value if value is not None else base_types.UninitialisedField(self, 'DspnsdNb', Number, False)

	@DspnsdNb.deleter
	def DspnsdNb(self):
		del self._DspnsdNb
		self._DspnsdNb = base_types.UninitialisedField(self, 'DspnsdNb', Number, False)

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if value is not None else base_types.UninitialisedField(self, 'InitlAmt', ImpliedCurrencyAndAmount, False)

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = base_types.UninitialisedField(self, 'InitlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def InitlNb(self):
		return self._InitlNb

	@InitlNb.setter
	def InitlNb(self, value):
		self._InitlNb = value if value is not None else base_types.UninitialisedField(self, 'InitlNb', Number, False)

	@InitlNb.deleter
	def InitlNb(self):
		del self._InitlNb
		self._InitlNb = base_types.UninitialisedField(self, 'InitlNb', Number, False)

	@property
	def PresntdNb(self):
		return self._PresntdNb

	@PresntdNb.setter
	def PresntdNb(self, value):
		self._PresntdNb = value if value is not None else base_types.UninitialisedField(self, 'PresntdNb', Number, False)

	@PresntdNb.deleter
	def PresntdNb(self):
		del self._PresntdNb
		self._PresntdNb = base_types.UninitialisedField(self, 'PresntdNb', Number, False)

	@property
	def RcycldNb(self):
		return self._RcycldNb

	@RcycldNb.setter
	def RcycldNb(self, value):
		self._RcycldNb = value if value is not None else base_types.UninitialisedField(self, 'RcycldNb', Number, False)

	@RcycldNb.deleter
	def RcycldNb(self):
		del self._RcycldNb
		self._RcycldNb = base_types.UninitialisedField(self, 'RcycldNb', Number, False)

	@property
	def RjctdNb(self):
		return self._RjctdNb

	@RjctdNb.setter
	def RjctdNb(self, value):
		self._RjctdNb = value if value is not None else base_types.UninitialisedField(self, 'RjctdNb', Number, False)

	@RjctdNb.deleter
	def RjctdNb(self):
		del self._RjctdNb
		self._RjctdNb = base_types.UninitialisedField(self, 'RjctdNb', Number, False)

	@property
	def RmvdAmt(self):
		return self._RmvdAmt

	@RmvdAmt.setter
	def RmvdAmt(self, value):
		self._RmvdAmt = value if value is not None else base_types.UninitialisedField(self, 'RmvdAmt', ImpliedCurrencyAndAmount, False)

	@RmvdAmt.deleter
	def RmvdAmt(self):
		del self._RmvdAmt
		self._RmvdAmt = base_types.UninitialisedField(self, 'RmvdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def RmvdNb(self):
		return self._RmvdNb

	@RmvdNb.setter
	def RmvdNb(self, value):
		self._RmvdNb = value if value is not None else base_types.UninitialisedField(self, 'RmvdNb', Number, False)

	@RmvdNb.deleter
	def RmvdNb(self):
		del self._RmvdNb
		self._RmvdNb = base_types.UninitialisedField(self, 'RmvdNb', Number, False)

	@property
	def RtrctdAmt(self):
		return self._RtrctdAmt

	@RtrctdAmt.setter
	def RtrctdAmt(self, value):
		self._RtrctdAmt = value if value is not None else base_types.UninitialisedField(self, 'RtrctdAmt', ImpliedCurrencyAndAmount, False)

	@RtrctdAmt.deleter
	def RtrctdAmt(self):
		del self._RtrctdAmt
		self._RtrctdAmt = base_types.UninitialisedField(self, 'RtrctdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def RtrctdNb(self):
		return self._RtrctdNb

	@RtrctdNb.setter
	def RtrctdNb(self, value):
		self._RtrctdNb = value if value is not None else base_types.UninitialisedField(self, 'RtrctdNb', Number, False)

	@RtrctdNb.deleter
	def RtrctdNb(self):
		del self._RtrctdNb
		self._RtrctdNb = base_types.UninitialisedField(self, 'RtrctdNb', Number, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ATMCounterType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ATMCounterType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddedNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DspnsdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcycldNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrctdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrctdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCounterType3Code, min=1, max=1, mutex_group=None, array=False),
	))