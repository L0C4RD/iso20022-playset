# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import Max70Text
from . import PartyIdentification27
from . import TradeCertificateType1Code
from . import YesNoIndicator

class RequiredSubmission4(base_types._BaseFieldType):

	__slots__ = ["_AuthrsdInspctrInd", "_CertTp", "_LineItmId", "_MtchConsgn", "_MtchInspctnDt", "_MtchIsseDt", "_MtchIssr", "_MtchManfctr", "_Submitr"]
	@property
	def AuthrsdInspctrInd(self):
		return self._AuthrsdInspctrInd

	@AuthrsdInspctrInd.setter
	def AuthrsdInspctrInd(self, value):
		self._AuthrsdInspctrInd = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdInspctrInd', YesNoIndicator, False)

	@AuthrsdInspctrInd.deleter
	def AuthrsdInspctrInd(self):
		del self._AuthrsdInspctrInd
		self._AuthrsdInspctrInd = base_types.UninitialisedField(self, 'AuthrsdInspctrInd', YesNoIndicator, False)

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if value is not None else base_types.UninitialisedField(self, 'CertTp', TradeCertificateType1Code, False)

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = base_types.UninitialisedField(self, 'CertTp', TradeCertificateType1Code, False)

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if value is not None else base_types.UninitialisedField(self, 'LineItmId', Max70Text, True)

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = base_types.UninitialisedField(self, 'LineItmId', Max70Text, True)

	@property
	def MtchConsgn(self):
		return self._MtchConsgn

	@MtchConsgn.setter
	def MtchConsgn(self, value):
		self._MtchConsgn = value if value is not None else base_types.UninitialisedField(self, 'MtchConsgn', YesNoIndicator, False)

	@MtchConsgn.deleter
	def MtchConsgn(self):
		del self._MtchConsgn
		self._MtchConsgn = base_types.UninitialisedField(self, 'MtchConsgn', YesNoIndicator, False)

	@property
	def MtchInspctnDt(self):
		return self._MtchInspctnDt

	@MtchInspctnDt.setter
	def MtchInspctnDt(self, value):
		self._MtchInspctnDt = value if value is not None else base_types.UninitialisedField(self, 'MtchInspctnDt', YesNoIndicator, False)

	@MtchInspctnDt.deleter
	def MtchInspctnDt(self):
		del self._MtchInspctnDt
		self._MtchInspctnDt = base_types.UninitialisedField(self, 'MtchInspctnDt', YesNoIndicator, False)

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
	def MtchManfctr(self):
		return self._MtchManfctr

	@MtchManfctr.setter
	def MtchManfctr(self, value):
		self._MtchManfctr = value if value is not None else base_types.UninitialisedField(self, 'MtchManfctr', PartyIdentification27, False)

	@MtchManfctr.deleter
	def MtchManfctr(self):
		del self._MtchManfctr
		self._MtchManfctr = base_types.UninitialisedField(self, 'MtchManfctr', PartyIdentification27, False)

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
		base_types.FieldEntry(name='AuthrsdInspctrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTp', type=TradeCertificateType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchConsgn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchInspctnDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIsseDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIssr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchManfctr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))