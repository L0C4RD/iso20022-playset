# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification176
from . import ISODateTime
from . import MaintenanceDelegation17
from . import Max140Binary

class MaintenanceDelegationResponse8(base_types._BaseFieldType):

	__slots__ = ["_DlgtnRspn", "_MstrTMId", "_TMChllngVal", "_TMDtTm", "_TMId"]
	@property
	def DlgtnRspn(self):
		return self._DlgtnRspn

	@DlgtnRspn.setter
	def DlgtnRspn(self, value):
		self._DlgtnRspn = value if value is not None else base_types.UninitialisedField(self, 'DlgtnRspn', MaintenanceDelegation17, True)

	@DlgtnRspn.deleter
	def DlgtnRspn(self):
		del self._DlgtnRspn
		self._DlgtnRspn = base_types.UninitialisedField(self, 'DlgtnRspn', MaintenanceDelegation17, True)

	@property
	def MstrTMId(self):
		return self._MstrTMId

	@MstrTMId.setter
	def MstrTMId(self, value):
		self._MstrTMId = value if value is not None else base_types.UninitialisedField(self, 'MstrTMId', GenericIdentification176, False)

	@MstrTMId.deleter
	def MstrTMId(self):
		del self._MstrTMId
		self._MstrTMId = base_types.UninitialisedField(self, 'MstrTMId', GenericIdentification176, False)

	@property
	def TMChllngVal(self):
		return self._TMChllngVal

	@TMChllngVal.setter
	def TMChllngVal(self, value):
		self._TMChllngVal = value if value is not None else base_types.UninitialisedField(self, 'TMChllngVal', Max140Binary, False)

	@TMChllngVal.deleter
	def TMChllngVal(self):
		del self._TMChllngVal
		self._TMChllngVal = base_types.UninitialisedField(self, 'TMChllngVal', Max140Binary, False)

	@property
	def TMDtTm(self):
		return self._TMDtTm

	@TMDtTm.setter
	def TMDtTm(self, value):
		self._TMDtTm = value if value is not None else base_types.UninitialisedField(self, 'TMDtTm', ISODateTime, False)

	@TMDtTm.deleter
	def TMDtTm(self):
		del self._TMDtTm
		self._TMDtTm = base_types.UninitialisedField(self, 'TMDtTm', ISODateTime, False)

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if value is not None else base_types.UninitialisedField(self, 'TMId', GenericIdentification176, False)

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = base_types.UninitialisedField(self, 'TMId', GenericIdentification176, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtnRspn', type=MaintenanceDelegation17, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrTMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))