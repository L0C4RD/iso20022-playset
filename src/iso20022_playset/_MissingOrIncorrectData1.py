# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AMLIndicator import AMLIndicator
from ._UnableToApplyIncorrect2 import UnableToApplyIncorrect2
from ._UnableToApplyMissing2 import UnableToApplyMissing2

class MissingOrIncorrectData1(base_types._BaseFieldType):

	__slots__ = ["_AMLReq", "_IncrrctInf", "_MssngInf"]
	@property
	def AMLReq(self):
		return self._AMLReq

	@AMLReq.setter
	def AMLReq(self, value):
		self._AMLReq = value if type(value) != base_types.auto else self.make_default("AMLReq")

	@AMLReq.deleter
	def AMLReq(self):
		del self._AMLReq
		self._AMLReq = None

	@property
	def IncrrctInf(self):
		return self._IncrrctInf

	@IncrrctInf.setter
	def IncrrctInf(self, value):
		self._IncrrctInf = value if type(value) != base_types.auto else self.make_default("IncrrctInf")

	@IncrrctInf.deleter
	def IncrrctInf(self):
		del self._IncrrctInf
		self._IncrrctInf = None

	@property
	def MssngInf(self):
		return self._MssngInf

	@MssngInf.setter
	def MssngInf(self, value):
		self._MssngInf = value if type(value) != base_types.auto else self.make_default("MssngInf")

	@MssngInf.deleter
	def MssngInf(self):
		del self._MssngInf
		self._MssngInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AMLReq', type=AMLIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrrctInf', type=UnableToApplyIncorrect2, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='MssngInf', type=UnableToApplyMissing2, min=0, max=10, mutex_group=None, array=True),
	))