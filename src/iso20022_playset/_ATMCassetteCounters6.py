# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassetteCounters5
from . import ATMMediaType3Code
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Number

class ATMCassetteCounters6(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CurAmt", "_CurNb", "_FlowTtls", "_InitlCnt", "_MdiaCtgy", "_UnitVal"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CurAmt(self):
		return self._CurAmt

	@CurAmt.setter
	def CurAmt(self, value):
		self._CurAmt = value if value is not None else base_types.UninitialisedField(self, 'CurAmt', ImpliedCurrencyAndAmount, False)

	@CurAmt.deleter
	def CurAmt(self):
		del self._CurAmt
		self._CurAmt = base_types.UninitialisedField(self, 'CurAmt', ImpliedCurrencyAndAmount, False)

	@property
	def CurNb(self):
		return self._CurNb

	@CurNb.setter
	def CurNb(self, value):
		self._CurNb = value if value is not None else base_types.UninitialisedField(self, 'CurNb', Number, False)

	@CurNb.deleter
	def CurNb(self):
		del self._CurNb
		self._CurNb = base_types.UninitialisedField(self, 'CurNb', Number, False)

	@property
	def FlowTtls(self):
		return self._FlowTtls

	@FlowTtls.setter
	def FlowTtls(self, value):
		self._FlowTtls = value if value is not None else base_types.UninitialisedField(self, 'FlowTtls', ATMCassetteCounters5, True)

	@FlowTtls.deleter
	def FlowTtls(self):
		del self._FlowTtls
		self._FlowTtls = base_types.UninitialisedField(self, 'FlowTtls', ATMCassetteCounters5, True)

	@property
	def InitlCnt(self):
		return self._InitlCnt

	@InitlCnt.setter
	def InitlCnt(self, value):
		self._InitlCnt = value if value is not None else base_types.UninitialisedField(self, 'InitlCnt', Number, False)

	@InitlCnt.deleter
	def InitlCnt(self):
		del self._InitlCnt
		self._InitlCnt = base_types.UninitialisedField(self, 'InitlCnt', Number, False)

	@property
	def MdiaCtgy(self):
		return self._MdiaCtgy

	@MdiaCtgy.setter
	def MdiaCtgy(self, value):
		self._MdiaCtgy = value if value is not None else base_types.UninitialisedField(self, 'MdiaCtgy', ATMMediaType3Code, False)

	@MdiaCtgy.deleter
	def MdiaCtgy(self):
		del self._MdiaCtgy
		self._MdiaCtgy = base_types.UninitialisedField(self, 'MdiaCtgy', ATMMediaType3Code, False)

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if value is not None else base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlowTtls', type=ATMCassetteCounters5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitlCnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaCtgy', type=ATMMediaType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))