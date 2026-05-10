import base_types
import PercentageRate
import PartyIdentification15

class BasicCollateralValuation1Details(base_types._BaseFieldType):

	__slots__ = ["_ValtnHrcut", "_HrcutSrc"]
	@property
	def ValtnHrcut(self):
		return self._ValtnHrcut

	@ValtnHrcut.setter
	def ValtnHrcut(self, value):
		self._ValtnHrcut = value if type(value) != auto else self.make_default("ValtnHrcut")

	@ValtnHrcut.deleter
	def ValtnHrcut(self):
		del self._ValtnHrcut
		self._ValtnHrcut = None

	@property
	def HrcutSrc(self):
		return self._HrcutSrc

	@HrcutSrc.setter
	def HrcutSrc(self, value):
		self._HrcutSrc = value if type(value) != auto else self.make_default("HrcutSrc")

	@HrcutSrc.deleter
	def HrcutSrc(self):
		del self._HrcutSrc
		self._HrcutSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValtnHrcut', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrcutSrc', type=PartyIdentification15, min=0, max=1, mutex_group=None, array=False),
	))

