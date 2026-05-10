from . import base_types
from ._Max35Text import Max35Text
from ._ActivationStatus2Code import ActivationStatus2Code
from ._Max70Text import Max70Text

class ATMVersionReport1(base_types._BaseFieldType):

	__slots__ = ["_FailRsn", "_CfgtnSts", "_CfgtnVrsn"]
	@property
	def CfgtnSts(self):
		return self._CfgtnSts

	@CfgtnSts.setter
	def CfgtnSts(self, value):
		self._CfgtnSts = value if type(value) != base_types.auto else self.make_default("CfgtnSts")

	@CfgtnSts.deleter
	def CfgtnSts(self):
		del self._CfgtnSts
		self._CfgtnSts = None

	@property
	def CfgtnVrsn(self):
		return self._CfgtnVrsn

	@CfgtnVrsn.setter
	def CfgtnVrsn(self, value):
		self._CfgtnVrsn = value if type(value) != base_types.auto else self.make_default("CfgtnVrsn")

	@CfgtnVrsn.deleter
	def CfgtnVrsn(self):
		del self._CfgtnVrsn
		self._CfgtnVrsn = None

	@property
	def FailRsn(self):
		return self._FailRsn

	@FailRsn.setter
	def FailRsn(self, value):
		self._FailRsn = value if type(value) != base_types.auto else self.make_default("FailRsn")

	@FailRsn.deleter
	def FailRsn(self):
		del self._FailRsn
		self._FailRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CfgtnSts', type=ActivationStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CfgtnVrsn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailRsn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

