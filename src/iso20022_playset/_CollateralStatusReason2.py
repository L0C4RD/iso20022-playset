# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import Status10Code
from . import StatusReasonInformation13

class CollateralStatusReason2(base_types._BaseFieldType):

	__slots__ = ["_ElgbltySetPrfl", "_Rsn", "_Sts"]
	@property
	def ElgbltySetPrfl(self):
		return self._ElgbltySetPrfl

	@ElgbltySetPrfl.setter
	def ElgbltySetPrfl(self, value):
		self._ElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@ElgbltySetPrfl.deleter
	def ElgbltySetPrfl(self):
		del self._ElgbltySetPrfl
		self._ElgbltySetPrfl = base_types.UninitialisedField(self, 'ElgbltySetPrfl', GenericIdentification1, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', StatusReasonInformation13, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', StatusReasonInformation13, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Status10Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Status10Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgbltySetPrfl', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=StatusReasonInformation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Status10Code, min=1, max=1, mutex_group=None, array=False),
	))