# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification176
from . import ISODateTime
from . import MaintenanceDelegation20
from . import Max140Binary

class MaintenanceDelegationRequest12(base_types._BaseFieldType):

	__slots__ = ["_MstrTMId", "_ReqdDlgtn", "_TMChllngVal", "_TMDtTm", "_TMId"]
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
	def ReqdDlgtn(self):
		return self._ReqdDlgtn

	@ReqdDlgtn.setter
	def ReqdDlgtn(self, value):
		self._ReqdDlgtn = value if value is not None else base_types.UninitialisedField(self, 'ReqdDlgtn', MaintenanceDelegation20, True)

	@ReqdDlgtn.deleter
	def ReqdDlgtn(self):
		del self._ReqdDlgtn
		self._ReqdDlgtn = base_types.UninitialisedField(self, 'ReqdDlgtn', MaintenanceDelegation20, True)

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
		base_types.FieldEntry(name='MstrTMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdDlgtn', type=MaintenanceDelegation20, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))