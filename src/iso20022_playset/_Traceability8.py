# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification177
from . import ISODateTime
from . import Max35Text
from . import Max6Text

class Traceability8(base_types._BaseFieldType):

	__slots__ = ["_PrtcolNm", "_PrtcolVrsn", "_RlayId", "_TracDtTmIn", "_TracDtTmOut"]
	@property
	def PrtcolNm(self):
		return self._PrtcolNm

	@PrtcolNm.setter
	def PrtcolNm(self, value):
		self._PrtcolNm = value if value is not None else base_types.UninitialisedField(self, 'PrtcolNm', Max35Text, False)

	@PrtcolNm.deleter
	def PrtcolNm(self):
		del self._PrtcolNm
		self._PrtcolNm = base_types.UninitialisedField(self, 'PrtcolNm', Max35Text, False)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max6Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max6Text, False)

	@property
	def RlayId(self):
		return self._RlayId

	@RlayId.setter
	def RlayId(self, value):
		self._RlayId = value if value is not None else base_types.UninitialisedField(self, 'RlayId', GenericIdentification177, False)

	@RlayId.deleter
	def RlayId(self):
		del self._RlayId
		self._RlayId = base_types.UninitialisedField(self, 'RlayId', GenericIdentification177, False)

	@property
	def TracDtTmIn(self):
		return self._TracDtTmIn

	@TracDtTmIn.setter
	def TracDtTmIn(self, value):
		self._TracDtTmIn = value if value is not None else base_types.UninitialisedField(self, 'TracDtTmIn', ISODateTime, False)

	@TracDtTmIn.deleter
	def TracDtTmIn(self):
		del self._TracDtTmIn
		self._TracDtTmIn = base_types.UninitialisedField(self, 'TracDtTmIn', ISODateTime, False)

	@property
	def TracDtTmOut(self):
		return self._TracDtTmOut

	@TracDtTmOut.setter
	def TracDtTmOut(self, value):
		self._TracDtTmOut = value if value is not None else base_types.UninitialisedField(self, 'TracDtTmOut', ISODateTime, False)

	@TracDtTmOut.deleter
	def TracDtTmOut(self):
		del self._TracDtTmOut
		self._TracDtTmOut = base_types.UninitialisedField(self, 'TracDtTmOut', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtcolNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlayId', type=GenericIdentification177, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmIn', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmOut', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))