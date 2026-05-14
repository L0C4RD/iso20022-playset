# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._Percentage14Rate import Percentage14Rate

class AdditionalRightThreshold2Choice(base_types._BaseFieldType):

	__slots__ = ["_AddtlRghtThrshld", "_AddtlRghtThrshldPctg"]
	@property
	def AddtlRghtThrshld(self):
		return self._AddtlRghtThrshld

	@AddtlRghtThrshld.setter
	def AddtlRghtThrshld(self, value):
		self._AddtlRghtThrshld = value if type(value) != base_types.auto else self.make_default("AddtlRghtThrshld")

	@AddtlRghtThrshld.deleter
	def AddtlRghtThrshld(self):
		del self._AddtlRghtThrshld
		self._AddtlRghtThrshld = None

	@property
	def AddtlRghtThrshldPctg(self):
		return self._AddtlRghtThrshldPctg

	@AddtlRghtThrshldPctg.setter
	def AddtlRghtThrshldPctg(self, value):
		self._AddtlRghtThrshldPctg = value if type(value) != base_types.auto else self.make_default("AddtlRghtThrshldPctg")

	@AddtlRghtThrshldPctg.deleter
	def AddtlRghtThrshldPctg(self):
		del self._AddtlRghtThrshldPctg
		self._AddtlRghtThrshldPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRghtThrshld', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlRghtThrshldPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))