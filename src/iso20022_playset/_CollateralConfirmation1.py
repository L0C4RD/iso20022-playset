# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralSubstitutionConfirmation1Code
from . import Max140Text
from . import Max35Text

class CollateralConfirmation1(base_types._BaseFieldType):

	__slots__ = ["_Cmnt", "_CollSbstitnReqId", "_CollSbstitnRspnId", "_ConfTp"]
	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if value is not None else base_types.UninitialisedField(self, 'Cmnt', Max140Text, False)

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = base_types.UninitialisedField(self, 'Cmnt', Max140Text, False)

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@property
	def CollSbstitnRspnId(self):
		return self._CollSbstitnRspnId

	@CollSbstitnRspnId.setter
	def CollSbstitnRspnId(self, value):
		self._CollSbstitnRspnId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	@CollSbstitnRspnId.deleter
	def CollSbstitnRspnId(self):
		del self._CollSbstitnRspnId
		self._CollSbstitnRspnId = base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	@property
	def ConfTp(self):
		return self._ConfTp

	@ConfTp.setter
	def ConfTp(self, value):
		self._ConfTp = value if value is not None else base_types.UninitialisedField(self, 'ConfTp', CollateralSubstitutionConfirmation1Code, False)

	@ConfTp.deleter
	def ConfTp(self):
		del self._ConfTp
		self._ConfTp = base_types.UninitialisedField(self, 'ConfTp', CollateralSubstitutionConfirmation1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmnt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfTp', type=CollateralSubstitutionConfirmation1Code, min=1, max=1, mutex_group=None, array=False),
	))