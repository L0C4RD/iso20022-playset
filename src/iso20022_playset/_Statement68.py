# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Number3Choice
from . import RestrictedFINXMax16Text
from . import UpdateType16Choice
from . import YesNoIndicator

class Statement68(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_CtrPtyPrtflTrfNtfctnRef", "_RptNb", "_StmtDtTm", "_StmtId", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def CtrPtyPrtflTrfNtfctnRef(self):
		return self._CtrPtyPrtflTrfNtfctnRef

	@CtrPtyPrtflTrfNtfctnRef.setter
	def CtrPtyPrtflTrfNtfctnRef(self, value):
		self._CtrPtyPrtflTrfNtfctnRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyPrtflTrfNtfctnRef', RestrictedFINXMax16Text, False)

	@CtrPtyPrtflTrfNtfctnRef.deleter
	def CtrPtyPrtflTrfNtfctnRef(self):
		del self._CtrPtyPrtflTrfNtfctnRef
		self._CtrPtyPrtflTrfNtfctnRef = base_types.UninitialisedField(self, 'CtrPtyPrtflTrfNtfctnRef', RestrictedFINXMax16Text, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTime2Choice, False)

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTime2Choice, False)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', RestrictedFINXMax16Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', RestrictedFINXMax16Text, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType16Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType16Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyPrtflTrfNtfctnRef', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType16Choice, min=0, max=1, mutex_group=None, array=False),
	))