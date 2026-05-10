import base_types
import ImpliedCurrencyAndAmount
import ATMCounterType3Code
import Number

class ATMCassetteCounters5(base_types._BaseFieldType):

	__slots__ = ["_RcycldNb", "_RjctdNb", "_InitlAmt", "_AddedNb", "_RmvdNb", "_RtrctdNb", "_RtrctdAmt", "_InitlNb", "_PresntdNb", "_Tp", "_DpstdNb", "_DpstdAmt", "_DspnsdNb", "_RmvdAmt"]
	@property
	def RcycldNb(self):
		return self._RcycldNb

	@RcycldNb.setter
	def RcycldNb(self, value):
		self._RcycldNb = value if type(value) != auto else self.make_default("RcycldNb")

	@RcycldNb.deleter
	def RcycldNb(self):
		del self._RcycldNb
		self._RcycldNb = None

	@property
	def RjctdNb(self):
		return self._RjctdNb

	@RjctdNb.setter
	def RjctdNb(self, value):
		self._RjctdNb = value if type(value) != auto else self.make_default("RjctdNb")

	@RjctdNb.deleter
	def RjctdNb(self):
		del self._RjctdNb
		self._RjctdNb = None

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if type(value) != auto else self.make_default("InitlAmt")

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = None

	@property
	def AddedNb(self):
		return self._AddedNb

	@AddedNb.setter
	def AddedNb(self, value):
		self._AddedNb = value if type(value) != auto else self.make_default("AddedNb")

	@AddedNb.deleter
	def AddedNb(self):
		del self._AddedNb
		self._AddedNb = None

	@property
	def RmvdNb(self):
		return self._RmvdNb

	@RmvdNb.setter
	def RmvdNb(self, value):
		self._RmvdNb = value if type(value) != auto else self.make_default("RmvdNb")

	@RmvdNb.deleter
	def RmvdNb(self):
		del self._RmvdNb
		self._RmvdNb = None

	@property
	def RtrctdNb(self):
		return self._RtrctdNb

	@RtrctdNb.setter
	def RtrctdNb(self, value):
		self._RtrctdNb = value if type(value) != auto else self.make_default("RtrctdNb")

	@RtrctdNb.deleter
	def RtrctdNb(self):
		del self._RtrctdNb
		self._RtrctdNb = None

	@property
	def RtrctdAmt(self):
		return self._RtrctdAmt

	@RtrctdAmt.setter
	def RtrctdAmt(self, value):
		self._RtrctdAmt = value if type(value) != auto else self.make_default("RtrctdAmt")

	@RtrctdAmt.deleter
	def RtrctdAmt(self):
		del self._RtrctdAmt
		self._RtrctdAmt = None

	@property
	def InitlNb(self):
		return self._InitlNb

	@InitlNb.setter
	def InitlNb(self, value):
		self._InitlNb = value if type(value) != auto else self.make_default("InitlNb")

	@InitlNb.deleter
	def InitlNb(self):
		del self._InitlNb
		self._InitlNb = None

	@property
	def PresntdNb(self):
		return self._PresntdNb

	@PresntdNb.setter
	def PresntdNb(self, value):
		self._PresntdNb = value if type(value) != auto else self.make_default("PresntdNb")

	@PresntdNb.deleter
	def PresntdNb(self):
		del self._PresntdNb
		self._PresntdNb = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DpstdNb(self):
		return self._DpstdNb

	@DpstdNb.setter
	def DpstdNb(self, value):
		self._DpstdNb = value if type(value) != auto else self.make_default("DpstdNb")

	@DpstdNb.deleter
	def DpstdNb(self):
		del self._DpstdNb
		self._DpstdNb = None

	@property
	def DpstdAmt(self):
		return self._DpstdAmt

	@DpstdAmt.setter
	def DpstdAmt(self, value):
		self._DpstdAmt = value if type(value) != auto else self.make_default("DpstdAmt")

	@DpstdAmt.deleter
	def DpstdAmt(self):
		del self._DpstdAmt
		self._DpstdAmt = None

	@property
	def DspnsdNb(self):
		return self._DspnsdNb

	@DspnsdNb.setter
	def DspnsdNb(self, value):
		self._DspnsdNb = value if type(value) != auto else self.make_default("DspnsdNb")

	@DspnsdNb.deleter
	def DspnsdNb(self):
		del self._DspnsdNb
		self._DspnsdNb = None

	@property
	def RmvdAmt(self):
		return self._RmvdAmt

	@RmvdAmt.setter
	def RmvdAmt(self, value):
		self._RmvdAmt = value if type(value) != auto else self.make_default("RmvdAmt")

	@RmvdAmt.deleter
	def RmvdAmt(self):
		del self._RmvdAmt
		self._RmvdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcycldNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddedNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrctdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrctdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCounterType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DspnsdNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

