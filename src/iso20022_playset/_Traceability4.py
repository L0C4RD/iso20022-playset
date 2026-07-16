# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification77
from . import ISODateTime
from . import Max35Text

class Traceability4(base_types._BaseFieldType):

	__slots__ = ["_RlayId", "_SeqNb", "_TracDtTmIn", "_TracDtTmOut"]
	@property
	def RlayId(self):
		return self._RlayId

	@RlayId.setter
	def RlayId(self, value):
		self._RlayId = value if value is not None else base_types.UninitialisedField(self, 'RlayId', GenericIdentification77, False)

	@RlayId.deleter
	def RlayId(self):
		del self._RlayId
		self._RlayId = base_types.UninitialisedField(self, 'RlayId', GenericIdentification77, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max35Text, False)

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
		base_types.FieldEntry(name='RlayId', type=GenericIdentification77, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmIn', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracDtTmOut', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))