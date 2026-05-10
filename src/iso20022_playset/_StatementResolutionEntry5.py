from . import base_types
from .Max35Text import Max35Text
from .OriginalGroupInformation29 import OriginalGroupInformation29
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .UUIDv4Identifier import UUIDv4Identifier
from .Purpose2Choice import Purpose2Choice
from .Charges15 import Charges15

class StatementResolutionEntry5(base_types._BaseFieldType):

	__slots__ = ["_CrrctdAmt", "_Chrgs", "_AcctSvcrRef", "_Purp", "_OrgnlGrpInf", "_UETR", "_OrgnlStmtId"]
	@property
	def CrrctdAmt(self):
		return self._CrrctdAmt

	@CrrctdAmt.setter
	def CrrctdAmt(self, value):
		self._CrrctdAmt = value if type(value) != base_types.auto else self.make_default("CrrctdAmt")

	@CrrctdAmt.deleter
	def CrrctdAmt(self):
		del self._CrrctdAmt
		self._CrrctdAmt = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if type(value) != base_types.auto else self.make_default("AcctSvcrRef")

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != base_types.auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if type(value) != base_types.auto else self.make_default("OrgnlStmtId")

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrctdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

