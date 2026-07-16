# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max52Text

class DisseminationData1(base_types._BaseFieldType):

	__slots__ = ["_DssmntnIdr", "_OrgnlDssmntnIdr", "_TmStmp"]
	@property
	def DssmntnIdr(self):
		return self._DssmntnIdr

	@DssmntnIdr.setter
	def DssmntnIdr(self, value):
		self._DssmntnIdr = value if value is not None else base_types.UninitialisedField(self, 'DssmntnIdr', Max52Text, False)

	@DssmntnIdr.deleter
	def DssmntnIdr(self):
		del self._DssmntnIdr
		self._DssmntnIdr = base_types.UninitialisedField(self, 'DssmntnIdr', Max52Text, False)

	@property
	def OrgnlDssmntnIdr(self):
		return self._OrgnlDssmntnIdr

	@OrgnlDssmntnIdr.setter
	def OrgnlDssmntnIdr(self, value):
		self._OrgnlDssmntnIdr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDssmntnIdr', Max52Text, False)

	@OrgnlDssmntnIdr.deleter
	def OrgnlDssmntnIdr(self):
		del self._OrgnlDssmntnIdr
		self._OrgnlDssmntnIdr = base_types.UninitialisedField(self, 'OrgnlDssmntnIdr', Max52Text, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DssmntnIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDssmntnIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))