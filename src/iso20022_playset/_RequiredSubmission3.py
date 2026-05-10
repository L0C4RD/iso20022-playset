from . import base_types
from ._InsuranceClauses1Code import InsuranceClauses1Code
from ._YesNoIndicator import YesNoIndicator
from ._PartyIdentification27 import PartyIdentification27
from ._AssuredType1Code import AssuredType1Code
from ._BICIdentification1 import BICIdentification1

class RequiredSubmission3(base_types._BaseFieldType):

	__slots__ = ["_MtchAmt", "_Submitr", "_MtchIsseDt", "_MtchTrnsprt", "_MtchAssrdPty", "_MtchIssr", "_ClausesReqrd"]
	@property
	def ClausesReqrd(self):
		return self._ClausesReqrd

	@ClausesReqrd.setter
	def ClausesReqrd(self, value):
		self._ClausesReqrd = value if type(value) != base_types.auto else self.make_default("ClausesReqrd")

	@ClausesReqrd.deleter
	def ClausesReqrd(self):
		del self._ClausesReqrd
		self._ClausesReqrd = None

	@property
	def MtchAmt(self):
		return self._MtchAmt

	@MtchAmt.setter
	def MtchAmt(self, value):
		self._MtchAmt = value if type(value) != base_types.auto else self.make_default("MtchAmt")

	@MtchAmt.deleter
	def MtchAmt(self):
		del self._MtchAmt
		self._MtchAmt = None

	@property
	def MtchAssrdPty(self):
		return self._MtchAssrdPty

	@MtchAssrdPty.setter
	def MtchAssrdPty(self, value):
		self._MtchAssrdPty = value if type(value) != base_types.auto else self.make_default("MtchAssrdPty")

	@MtchAssrdPty.deleter
	def MtchAssrdPty(self):
		del self._MtchAssrdPty
		self._MtchAssrdPty = None

	@property
	def MtchIsseDt(self):
		return self._MtchIsseDt

	@MtchIsseDt.setter
	def MtchIsseDt(self, value):
		self._MtchIsseDt = value if type(value) != base_types.auto else self.make_default("MtchIsseDt")

	@MtchIsseDt.deleter
	def MtchIsseDt(self):
		del self._MtchIsseDt
		self._MtchIsseDt = None

	@property
	def MtchIssr(self):
		return self._MtchIssr

	@MtchIssr.setter
	def MtchIssr(self, value):
		self._MtchIssr = value if type(value) != base_types.auto else self.make_default("MtchIssr")

	@MtchIssr.deleter
	def MtchIssr(self):
		del self._MtchIssr
		self._MtchIssr = None

	@property
	def MtchTrnsprt(self):
		return self._MtchTrnsprt

	@MtchTrnsprt.setter
	def MtchTrnsprt(self, value):
		self._MtchTrnsprt = value if type(value) != base_types.auto else self.make_default("MtchTrnsprt")

	@MtchTrnsprt.deleter
	def MtchTrnsprt(self):
		del self._MtchTrnsprt
		self._MtchTrnsprt = None

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if type(value) != base_types.auto else self.make_default("Submitr")

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClausesReqrd', type=InsuranceClauses1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchAmt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchAssrdPty', type=AssuredType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIsseDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIssr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchTrnsprt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))

