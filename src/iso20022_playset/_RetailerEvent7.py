# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EventContext7
from . import EventToNotify2Code
from . import ISODateTime
from . import Max1025Text

class RetailerEvent7(base_types._BaseFieldType):

	__slots__ = ["_AddtlEvtInf", "_EvtCntxt", "_EvtTmStmp", "_EvtToNtfy"]
	@property
	def AddtlEvtInf(self):
		return self._AddtlEvtInf

	@AddtlEvtInf.setter
	def AddtlEvtInf(self, value):
		self._AddtlEvtInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlEvtInf', Max1025Text, False)

	@AddtlEvtInf.deleter
	def AddtlEvtInf(self):
		del self._AddtlEvtInf
		self._AddtlEvtInf = base_types.UninitialisedField(self, 'AddtlEvtInf', Max1025Text, False)

	@property
	def EvtCntxt(self):
		return self._EvtCntxt

	@EvtCntxt.setter
	def EvtCntxt(self, value):
		self._EvtCntxt = value if value is not None else base_types.UninitialisedField(self, 'EvtCntxt', EventContext7, False)

	@EvtCntxt.deleter
	def EvtCntxt(self):
		del self._EvtCntxt
		self._EvtCntxt = base_types.UninitialisedField(self, 'EvtCntxt', EventContext7, False)

	@property
	def EvtTmStmp(self):
		return self._EvtTmStmp

	@EvtTmStmp.setter
	def EvtTmStmp(self, value):
		self._EvtTmStmp = value if value is not None else base_types.UninitialisedField(self, 'EvtTmStmp', ISODateTime, False)

	@EvtTmStmp.deleter
	def EvtTmStmp(self):
		del self._EvtTmStmp
		self._EvtTmStmp = base_types.UninitialisedField(self, 'EvtTmStmp', ISODateTime, False)

	@property
	def EvtToNtfy(self):
		return self._EvtToNtfy

	@EvtToNtfy.setter
	def EvtToNtfy(self, value):
		self._EvtToNtfy = value if value is not None else base_types.UninitialisedField(self, 'EvtToNtfy', EventToNotify2Code, False)

	@EvtToNtfy.deleter
	def EvtToNtfy(self):
		del self._EvtToNtfy
		self._EvtToNtfy = base_types.UninitialisedField(self, 'EvtToNtfy', EventToNotify2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlEvtInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtCntxt', type=EventContext7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtToNtfy', type=EventToNotify2Code, min=1, max=1, mutex_group=None, array=False),
	))