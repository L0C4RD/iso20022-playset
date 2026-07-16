# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max1000Text
from . import Max35Text
from . import Max4AlphaNumericText

class Event2(base_types._BaseFieldType):

	__slots__ = ["_EvtCd", "_EvtDesc", "_EvtParam", "_EvtTm"]
	@property
	def EvtCd(self):
		return self._EvtCd

	@EvtCd.setter
	def EvtCd(self, value):
		self._EvtCd = value if value is not None else base_types.UninitialisedField(self, 'EvtCd', Max4AlphaNumericText, False)

	@EvtCd.deleter
	def EvtCd(self):
		del self._EvtCd
		self._EvtCd = base_types.UninitialisedField(self, 'EvtCd', Max4AlphaNumericText, False)

	@property
	def EvtDesc(self):
		return self._EvtDesc

	@EvtDesc.setter
	def EvtDesc(self, value):
		self._EvtDesc = value if value is not None else base_types.UninitialisedField(self, 'EvtDesc', Max1000Text, False)

	@EvtDesc.deleter
	def EvtDesc(self):
		del self._EvtDesc
		self._EvtDesc = base_types.UninitialisedField(self, 'EvtDesc', Max1000Text, False)

	@property
	def EvtParam(self):
		return self._EvtParam

	@EvtParam.setter
	def EvtParam(self, value):
		self._EvtParam = value if value is not None else base_types.UninitialisedField(self, 'EvtParam', Max35Text, True)

	@EvtParam.deleter
	def EvtParam(self):
		del self._EvtParam
		self._EvtParam = base_types.UninitialisedField(self, 'EvtParam', Max35Text, True)

	@property
	def EvtTm(self):
		return self._EvtTm

	@EvtTm.setter
	def EvtTm(self, value):
		self._EvtTm = value if value is not None else base_types.UninitialisedField(self, 'EvtTm', ISODateTime, False)

	@EvtTm.deleter
	def EvtTm(self):
		del self._EvtTm
		self._EvtTm = base_types.UninitialisedField(self, 'EvtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtCd', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtParam', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))