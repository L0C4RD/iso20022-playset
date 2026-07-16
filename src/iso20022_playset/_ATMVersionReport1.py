# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivationStatus2Code
from . import Max35Text
from . import Max70Text

class ATMVersionReport1(base_types._BaseFieldType):

	__slots__ = ["_CfgtnSts", "_CfgtnVrsn", "_FailRsn"]
	@property
	def CfgtnSts(self):
		return self._CfgtnSts

	@CfgtnSts.setter
	def CfgtnSts(self, value):
		self._CfgtnSts = value if value is not None else base_types.UninitialisedField(self, 'CfgtnSts', ActivationStatus2Code, False)

	@CfgtnSts.deleter
	def CfgtnSts(self):
		del self._CfgtnSts
		self._CfgtnSts = base_types.UninitialisedField(self, 'CfgtnSts', ActivationStatus2Code, False)

	@property
	def CfgtnVrsn(self):
		return self._CfgtnVrsn

	@CfgtnVrsn.setter
	def CfgtnVrsn(self, value):
		self._CfgtnVrsn = value if value is not None else base_types.UninitialisedField(self, 'CfgtnVrsn', Max35Text, False)

	@CfgtnVrsn.deleter
	def CfgtnVrsn(self):
		del self._CfgtnVrsn
		self._CfgtnVrsn = base_types.UninitialisedField(self, 'CfgtnVrsn', Max35Text, False)

	@property
	def FailRsn(self):
		return self._FailRsn

	@FailRsn.setter
	def FailRsn(self, value):
		self._FailRsn = value if value is not None else base_types.UninitialisedField(self, 'FailRsn', Max70Text, False)

	@FailRsn.deleter
	def FailRsn(self):
		del self._FailRsn
		self._FailRsn = base_types.UninitialisedField(self, 'FailRsn', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CfgtnSts', type=ActivationStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CfgtnVrsn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailRsn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))