# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalReference8 import AdditionalReference8
from ._InvestmentFundOrder8 import InvestmentFundOrder8
from ._References62Choice import References62Choice

class MessageAndBusinessReference10(base_types._BaseFieldType):

	__slots__ = ["_OrdrRef", "_Ref", "_RltdRef"]
	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != base_types.auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRef', type=InvestmentFundOrder8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=References62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference8, min=0, max=1, mutex_group=None, array=False),
	))