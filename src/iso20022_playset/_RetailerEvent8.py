# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EventContext8 import EventContext8
from ._EventToNotify2Code import EventToNotify2Code
from ._ISODateTime import ISODateTime
from ._Max1025Text import Max1025Text

class RetailerEvent8(base_types._BaseFieldType):

	__slots__ = ["_AddtlEvtInf", "_EvtCntxt", "_EvtTmStmp", "_EvtToNtfy"]
	@property
	def AddtlEvtInf(self):
		return self._AddtlEvtInf

	@AddtlEvtInf.setter
	def AddtlEvtInf(self, value):
		self._AddtlEvtInf = value if type(value) != base_types.auto else self.make_default("AddtlEvtInf")

	@AddtlEvtInf.deleter
	def AddtlEvtInf(self):
		del self._AddtlEvtInf
		self._AddtlEvtInf = None

	@property
	def EvtCntxt(self):
		return self._EvtCntxt

	@EvtCntxt.setter
	def EvtCntxt(self, value):
		self._EvtCntxt = value if type(value) != base_types.auto else self.make_default("EvtCntxt")

	@EvtCntxt.deleter
	def EvtCntxt(self):
		del self._EvtCntxt
		self._EvtCntxt = None

	@property
	def EvtTmStmp(self):
		return self._EvtTmStmp

	@EvtTmStmp.setter
	def EvtTmStmp(self, value):
		self._EvtTmStmp = value if type(value) != base_types.auto else self.make_default("EvtTmStmp")

	@EvtTmStmp.deleter
	def EvtTmStmp(self):
		del self._EvtTmStmp
		self._EvtTmStmp = None

	@property
	def EvtToNtfy(self):
		return self._EvtToNtfy

	@EvtToNtfy.setter
	def EvtToNtfy(self, value):
		self._EvtToNtfy = value if type(value) != base_types.auto else self.make_default("EvtToNtfy")

	@EvtToNtfy.deleter
	def EvtToNtfy(self):
		del self._EvtToNtfy
		self._EvtToNtfy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlEvtInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtCntxt', type=EventContext8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtToNtfy', type=EventToNotify2Code, min=1, max=1, mutex_group=None, array=False),
	))