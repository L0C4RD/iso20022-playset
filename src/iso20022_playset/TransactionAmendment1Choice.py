import base_types
import CashAccount40
import PartyIdentification135
import ISODateTime
import AnyBICDec2014Identifier
import Remittance1
import BranchAndFinancialInstitutionIdentification6
import ActiveCurrencyAndAmount
import ISODate
import Max4Text
import BICFIDec2014Identifier
import Max140Text

class TransactionAmendment1Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Dt", "_BICFI", "_DtTm", "_CshAcct", "_Rmt", "_Cd", "_AnyBIC", "_Pty", "_Amt", "_Agt"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def Rmt(self):
		return self._Rmt

	@Rmt.setter
	def Rmt(self, value):
		self._Rmt = value if type(value) != auto else self.make_default("Rmt")

	@Rmt.deleter
	def Rmt(self):
		del self._Rmt
		self._Rmt = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=Max140Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rmt', type=Remittance1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=Max4Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification135, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=1, array=False),
	))

