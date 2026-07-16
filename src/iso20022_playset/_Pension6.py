# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import Max35Text
from . import PensionPolicy1
from . import PensionSchemeType3Choice
from . import PensionTransferScope1Choice
from . import TaxReference1
from . import YesNoIndicator

class Pension6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DrwdwnTrchId", "_Id", "_NonWrpprTrf", "_TaxRef", "_Tp", "_TrfScp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def DrwdwnTrchId(self):
		return self._DrwdwnTrchId

	@DrwdwnTrchId.setter
	def DrwdwnTrchId(self, value):
		self._DrwdwnTrchId = value if value is not None else base_types.UninitialisedField(self, 'DrwdwnTrchId', Max35Text, False)

	@DrwdwnTrchId.deleter
	def DrwdwnTrchId(self):
		del self._DrwdwnTrchId
		self._DrwdwnTrchId = base_types.UninitialisedField(self, 'DrwdwnTrchId', Max35Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PensionPolicy1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PensionPolicy1, False)

	@property
	def NonWrpprTrf(self):
		return self._NonWrpprTrf

	@NonWrpprTrf.setter
	def NonWrpprTrf(self, value):
		self._NonWrpprTrf = value if value is not None else base_types.UninitialisedField(self, 'NonWrpprTrf', YesNoIndicator, False)

	@NonWrpprTrf.deleter
	def NonWrpprTrf(self):
		del self._NonWrpprTrf
		self._NonWrpprTrf = base_types.UninitialisedField(self, 'NonWrpprTrf', YesNoIndicator, False)

	@property
	def TaxRef(self):
		return self._TaxRef

	@TaxRef.setter
	def TaxRef(self, value):
		self._TaxRef = value if value is not None else base_types.UninitialisedField(self, 'TaxRef', TaxReference1, True)

	@TaxRef.deleter
	def TaxRef(self):
		del self._TaxRef
		self._TaxRef = base_types.UninitialisedField(self, 'TaxRef', TaxReference1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PensionSchemeType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PensionSchemeType3Choice, False)

	@property
	def TrfScp(self):
		return self._TrfScp

	@TrfScp.setter
	def TrfScp(self, value):
		self._TrfScp = value if value is not None else base_types.UninitialisedField(self, 'TrfScp', PensionTransferScope1Choice, False)

	@TrfScp.deleter
	def TrfScp(self):
		del self._TrfScp
		self._TrfScp = base_types.UninitialisedField(self, 'TrfScp', PensionTransferScope1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrwdwnTrchId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PensionPolicy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWrpprTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRef', type=TaxReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=PensionSchemeType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfScp', type=PensionTransferScope1Choice, min=0, max=1, mutex_group=None, array=False),
	))