# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification15
from . import PercentageRate

class BasicCollateralValuation1Details(base_types._BaseFieldType):

	__slots__ = ["_HrcutSrc", "_ValtnHrcut"]
	@property
	def HrcutSrc(self):
		return self._HrcutSrc

	@HrcutSrc.setter
	def HrcutSrc(self, value):
		self._HrcutSrc = value if value is not None else base_types.UninitialisedField(self, 'HrcutSrc', PartyIdentification15, False)

	@HrcutSrc.deleter
	def HrcutSrc(self):
		del self._HrcutSrc
		self._HrcutSrc = base_types.UninitialisedField(self, 'HrcutSrc', PartyIdentification15, False)

	@property
	def ValtnHrcut(self):
		return self._ValtnHrcut

	@ValtnHrcut.setter
	def ValtnHrcut(self, value):
		self._ValtnHrcut = value if value is not None else base_types.UninitialisedField(self, 'ValtnHrcut', PercentageRate, False)

	@ValtnHrcut.deleter
	def ValtnHrcut(self):
		del self._ValtnHrcut
		self._ValtnHrcut = base_types.UninitialisedField(self, 'ValtnHrcut', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HrcutSrc', type=PartyIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnHrcut', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))