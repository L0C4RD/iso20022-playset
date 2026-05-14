from . import base_types
from ._ISODateTime import ISODateTime
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._Max4AlphaNumericText import Max4AlphaNumericText

class Event1(base_types._BaseFieldType):

	__slots__ = ["_EvtCd", "_EvtDesc", "_EvtParam", "_EvtTm"]
	@property
	def EvtCd(self):
		return self._EvtCd

	@EvtCd.setter
	def EvtCd(self, value):
		self._EvtCd = value if type(value) != base_types.auto else self.make_default("EvtCd")

	@EvtCd.deleter
	def EvtCd(self):
		del self._EvtCd
		self._EvtCd = None

	@property
	def EvtDesc(self):
		return self._EvtDesc

	@EvtDesc.setter
	def EvtDesc(self, value):
		self._EvtDesc = value if type(value) != base_types.auto else self.make_default("EvtDesc")

	@EvtDesc.deleter
	def EvtDesc(self):
		del self._EvtDesc
		self._EvtDesc = None

	@property
	def EvtParam(self):
		return self._EvtParam

	@EvtParam.setter
	def EvtParam(self, value):
		self._EvtParam = value if type(value) != base_types.auto else self.make_default("EvtParam")

	@EvtParam.deleter
	def EvtParam(self):
		del self._EvtParam
		self._EvtParam = None

	@property
	def EvtTm(self):
		return self._EvtTm

	@EvtTm.setter
	def EvtTm(self, value):
		self._EvtTm = value if type(value) != base_types.auto else self.make_default("EvtTm")

	@EvtTm.deleter
	def EvtTm(self):
		del self._EvtTm
		self._EvtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtCd', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtParam', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

