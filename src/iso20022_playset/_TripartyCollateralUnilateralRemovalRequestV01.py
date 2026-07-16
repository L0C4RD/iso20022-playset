# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralRole1Code
from . import Max35Text
from . import Pagination1
from . import PartyIdentification232
from . import RequestDetails28
from . import SupplementaryData1

class TripartyCollateralUnilateralRemovalRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ClntPtyA", "_CollSd", "_Pgntn", "_PtyA", "_ReqDtls", "_RmvlReqId", "_SplmtryData"]
	@property
	def ClntPtyA(self):
		return self._ClntPtyA

	@ClntPtyA.setter
	def ClntPtyA(self, value):
		self._ClntPtyA = value if value is not None else base_types.UninitialisedField(self, 'ClntPtyA', PartyIdentification232, False)

	@ClntPtyA.deleter
	def ClntPtyA(self):
		del self._ClntPtyA
		self._ClntPtyA = base_types.UninitialisedField(self, 'ClntPtyA', PartyIdentification232, False)

	@property
	def CollSd(self):
		return self._CollSd

	@CollSd.setter
	def CollSd(self, value):
		self._CollSd = value if value is not None else base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@CollSd.deleter
	def CollSd(self):
		del self._CollSd
		self._CollSd = base_types.UninitialisedField(self, 'CollSd', CollateralRole1Code, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if value is not None else base_types.UninitialisedField(self, 'PtyA', PartyIdentification232, False)

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = base_types.UninitialisedField(self, 'PtyA', PartyIdentification232, False)

	@property
	def ReqDtls(self):
		return self._ReqDtls

	@ReqDtls.setter
	def ReqDtls(self, value):
		self._ReqDtls = value if value is not None else base_types.UninitialisedField(self, 'ReqDtls', RequestDetails28, False)

	@ReqDtls.deleter
	def ReqDtls(self):
		del self._ReqDtls
		self._ReqDtls = base_types.UninitialisedField(self, 'ReqDtls', RequestDetails28, False)

	@property
	def RmvlReqId(self):
		return self._RmvlReqId

	@RmvlReqId.setter
	def RmvlReqId(self, value):
		self._RmvlReqId = value if value is not None else base_types.UninitialisedField(self, 'RmvlReqId', Max35Text, False)

	@RmvlReqId.deleter
	def RmvlReqId(self):
		del self._RmvlReqId
		self._RmvlReqId = base_types.UninitialisedField(self, 'RmvlReqId', Max35Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntPtyA', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSd', type=CollateralRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification232, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqDtls', type=RequestDetails28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
	))