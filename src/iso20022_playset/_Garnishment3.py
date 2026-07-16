# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import GarnishmentType1
from . import ISODate
from . import Max140Text
from . import PartyIdentification135
from . import TrueFalseIndicator

class Garnishment3(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_FmlyMdclInsrncInd", "_Grnshee", "_GrnshmtAdmstr", "_MplyeeTermntnInd", "_RefNb", "_RmtdAmt", "_Tp"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def FmlyMdclInsrncInd(self):
		return self._FmlyMdclInsrncInd

	@FmlyMdclInsrncInd.setter
	def FmlyMdclInsrncInd(self, value):
		self._FmlyMdclInsrncInd = value if value is not None else base_types.UninitialisedField(self, 'FmlyMdclInsrncInd', TrueFalseIndicator, False)

	@FmlyMdclInsrncInd.deleter
	def FmlyMdclInsrncInd(self):
		del self._FmlyMdclInsrncInd
		self._FmlyMdclInsrncInd = base_types.UninitialisedField(self, 'FmlyMdclInsrncInd', TrueFalseIndicator, False)

	@property
	def Grnshee(self):
		return self._Grnshee

	@Grnshee.setter
	def Grnshee(self, value):
		self._Grnshee = value if value is not None else base_types.UninitialisedField(self, 'Grnshee', PartyIdentification135, False)

	@Grnshee.deleter
	def Grnshee(self):
		del self._Grnshee
		self._Grnshee = base_types.UninitialisedField(self, 'Grnshee', PartyIdentification135, False)

	@property
	def GrnshmtAdmstr(self):
		return self._GrnshmtAdmstr

	@GrnshmtAdmstr.setter
	def GrnshmtAdmstr(self, value):
		self._GrnshmtAdmstr = value if value is not None else base_types.UninitialisedField(self, 'GrnshmtAdmstr', PartyIdentification135, False)

	@GrnshmtAdmstr.deleter
	def GrnshmtAdmstr(self):
		del self._GrnshmtAdmstr
		self._GrnshmtAdmstr = base_types.UninitialisedField(self, 'GrnshmtAdmstr', PartyIdentification135, False)

	@property
	def MplyeeTermntnInd(self):
		return self._MplyeeTermntnInd

	@MplyeeTermntnInd.setter
	def MplyeeTermntnInd(self, value):
		self._MplyeeTermntnInd = value if value is not None else base_types.UninitialisedField(self, 'MplyeeTermntnInd', TrueFalseIndicator, False)

	@MplyeeTermntnInd.deleter
	def MplyeeTermntnInd(self):
		del self._MplyeeTermntnInd
		self._MplyeeTermntnInd = base_types.UninitialisedField(self, 'MplyeeTermntnInd', TrueFalseIndicator, False)

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if value is not None else base_types.UninitialisedField(self, 'RefNb', Max140Text, False)

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = base_types.UninitialisedField(self, 'RefNb', Max140Text, False)

	@property
	def RmtdAmt(self):
		return self._RmtdAmt

	@RmtdAmt.setter
	def RmtdAmt(self, value):
		self._RmtdAmt = value if value is not None else base_types.UninitialisedField(self, 'RmtdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@RmtdAmt.deleter
	def RmtdAmt(self):
		del self._RmtdAmt
		self._RmtdAmt = base_types.UninitialisedField(self, 'RmtdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', GarnishmentType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', GarnishmentType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FmlyMdclInsrncInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grnshee', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrnshmtAdmstr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeeTermntnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GarnishmentType1, min=1, max=1, mutex_group=None, array=False),
	))