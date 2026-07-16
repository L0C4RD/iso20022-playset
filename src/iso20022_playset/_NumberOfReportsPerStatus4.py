# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import PairedReconciled3Code

class NumberOfReportsPerStatus4(base_types._BaseFieldType):

	__slots__ = ["_DtldNbOfRpts", "_DtldSts"]
	@property
	def DtldNbOfRpts(self):
		return self._DtldNbOfRpts

	@DtldNbOfRpts.setter
	def DtldNbOfRpts(self, value):
		self._DtldNbOfRpts = value if value is not None else base_types.UninitialisedField(self, 'DtldNbOfRpts', Max15NumericText, False)

	@DtldNbOfRpts.deleter
	def DtldNbOfRpts(self):
		del self._DtldNbOfRpts
		self._DtldNbOfRpts = base_types.UninitialisedField(self, 'DtldNbOfRpts', Max15NumericText, False)

	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if value is not None else base_types.UninitialisedField(self, 'DtldSts', PairedReconciled3Code, False)

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = base_types.UninitialisedField(self, 'DtldSts', PairedReconciled3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNbOfRpts', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldSts', type=PairedReconciled3Code, min=1, max=1, mutex_group=None, array=False),
	))