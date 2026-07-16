# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssuredType1Code
from . import BICIdentification1
from . import InsuranceClauses1Code
from . import PartyIdentification27
from . import YesNoIndicator

class RequiredSubmission3(base_types._BaseFieldType):

	__slots__ = ["_ClausesReqrd", "_MtchAmt", "_MtchAssrdPty", "_MtchIsseDt", "_MtchIssr", "_MtchTrnsprt", "_Submitr"]
	@property
	def ClausesReqrd(self):
		return self._ClausesReqrd

	@ClausesReqrd.setter
	def ClausesReqrd(self, value):
		self._ClausesReqrd = value if value is not None else base_types.UninitialisedField(self, 'ClausesReqrd', InsuranceClauses1Code, True)

	@ClausesReqrd.deleter
	def ClausesReqrd(self):
		del self._ClausesReqrd
		self._ClausesReqrd = base_types.UninitialisedField(self, 'ClausesReqrd', InsuranceClauses1Code, True)

	@property
	def MtchAmt(self):
		return self._MtchAmt

	@MtchAmt.setter
	def MtchAmt(self, value):
		self._MtchAmt = value if value is not None else base_types.UninitialisedField(self, 'MtchAmt', YesNoIndicator, False)

	@MtchAmt.deleter
	def MtchAmt(self):
		del self._MtchAmt
		self._MtchAmt = base_types.UninitialisedField(self, 'MtchAmt', YesNoIndicator, False)

	@property
	def MtchAssrdPty(self):
		return self._MtchAssrdPty

	@MtchAssrdPty.setter
	def MtchAssrdPty(self, value):
		self._MtchAssrdPty = value if value is not None else base_types.UninitialisedField(self, 'MtchAssrdPty', AssuredType1Code, False)

	@MtchAssrdPty.deleter
	def MtchAssrdPty(self):
		del self._MtchAssrdPty
		self._MtchAssrdPty = base_types.UninitialisedField(self, 'MtchAssrdPty', AssuredType1Code, False)

	@property
	def MtchIsseDt(self):
		return self._MtchIsseDt

	@MtchIsseDt.setter
	def MtchIsseDt(self, value):
		self._MtchIsseDt = value if value is not None else base_types.UninitialisedField(self, 'MtchIsseDt', YesNoIndicator, False)

	@MtchIsseDt.deleter
	def MtchIsseDt(self):
		del self._MtchIsseDt
		self._MtchIsseDt = base_types.UninitialisedField(self, 'MtchIsseDt', YesNoIndicator, False)

	@property
	def MtchIssr(self):
		return self._MtchIssr

	@MtchIssr.setter
	def MtchIssr(self, value):
		self._MtchIssr = value if value is not None else base_types.UninitialisedField(self, 'MtchIssr', PartyIdentification27, False)

	@MtchIssr.deleter
	def MtchIssr(self):
		del self._MtchIssr
		self._MtchIssr = base_types.UninitialisedField(self, 'MtchIssr', PartyIdentification27, False)

	@property
	def MtchTrnsprt(self):
		return self._MtchTrnsprt

	@MtchTrnsprt.setter
	def MtchTrnsprt(self, value):
		self._MtchTrnsprt = value if value is not None else base_types.UninitialisedField(self, 'MtchTrnsprt', YesNoIndicator, False)

	@MtchTrnsprt.deleter
	def MtchTrnsprt(self):
		del self._MtchTrnsprt
		self._MtchTrnsprt = base_types.UninitialisedField(self, 'MtchTrnsprt', YesNoIndicator, False)

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if value is not None else base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClausesReqrd', type=InsuranceClauses1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchAmt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchAssrdPty', type=AssuredType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIsseDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIssr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchTrnsprt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))