# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivityDetails1
from . import BICIdentification1
from . import DocumentIdentification5
from . import Max35Text
from . import PendingActivity2

class ActivityReportItems3(base_types._BaseFieldType):

	__slots__ = ["_PdgReqForActn", "_RptdItm", "_RptdNtty", "_TxId", "_UsrTxRef"]
	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if value is not None else base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, True)

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, True)

	@property
	def RptdItm(self):
		return self._RptdItm

	@RptdItm.setter
	def RptdItm(self, value):
		self._RptdItm = value if value is not None else base_types.UninitialisedField(self, 'RptdItm', ActivityDetails1, True)

	@RptdItm.deleter
	def RptdItm(self):
		del self._RptdItm
		self._RptdItm = base_types.UninitialisedField(self, 'RptdItm', ActivityDetails1, True)

	@property
	def RptdNtty(self):
		return self._RptdNtty

	@RptdNtty.setter
	def RptdNtty(self, value):
		self._RptdNtty = value if value is not None else base_types.UninitialisedField(self, 'RptdNtty', BICIdentification1, True)

	@RptdNtty.deleter
	def RptdNtty(self):
		del self._RptdNtty
		self._RptdNtty = base_types.UninitialisedField(self, 'RptdNtty', BICIdentification1, True)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if value is not None else base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, True)

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptdItm', type=ActivityDetails1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptdNtty', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))