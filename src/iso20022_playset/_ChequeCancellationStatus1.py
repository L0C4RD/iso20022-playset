# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChequeCancellationStatus1Choice import ChequeCancellationStatus1Choice
from ._ChequePartyRole1Code import ChequePartyRole1Code
from ._Max140Text import Max140Text

class ChequeCancellationStatus1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Orgtr", "_Sts"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != base_types.auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=ChequePartyRole1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ChequeCancellationStatus1Choice, min=1, max=1, mutex_group=None, array=False),
	))